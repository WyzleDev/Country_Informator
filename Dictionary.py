import requests
import click
import webbrowser
import os
import colorama
from colorama import Fore, Back
colorama.init()
def country_info(name):
    url = "https://restcountries.eu/rest/v2/name/{}".format(name)
    response = requests.request("GET", url)
    return response.json()


@click.command()
@click.argument('name')
def main(name):
    """A little tool that shows you the current information in a COUNTRY your choice.
    Provide the country name!"""
    country = country_info(name)
    print('\n',
          'Country: {}'.format(country[0]['name']),
          '\n',
          'Capital is: {}'.format(country[0]['capital']),
          '\n',
          'Population is : {}'.format(country[0]['population']),
          '\n',
          'Number of timezones: {}'.format(len(country[0]['timezones'])),
          '\n',
          'Calling codes: +{}'.format(country[0]['callingCodes'][0]),
          '\n',
          'Native currencies: {}{}'.format(country[0]['currencies'][0]['symbol'], country[0]['currencies'][0]['code'])
          )
    print('\n')
    ask = input('Do you want to open a picture of a flag in a browser?\n'
                '1.Yes\n'
                '2.No'
                '\n'
                '> ')

    if ask == '1':
        try:

            webbrowser.get('chrome').open_new(country[0]['flag'])
            print('[+] Opening url via chrome')

        except Exception as e:
            print(Fore.RED + f'[-]{e}')
            print(Fore.GREEN + f'[+] Starting default browser')
            webbrowser.register('Edge', None, webbrowser.BackgroundBrowser(
                'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
            ))
            webbrowser.get("Edge").open_new(country[0]['flag'])


    elif ask == "2":
        print(Fore.BLUE + "See ya! Bye-Bye!")
        exit(0)

    else:
        print('[X] Something went wrong! Please enter 1 or 2 to get correct answer!')

    os.system('pause')
    os.system('cls')


if __name__ == '__main__':
    main()
