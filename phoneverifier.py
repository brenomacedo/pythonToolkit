from phonenumbers import geocoder, parse

phone = str(input('Digite o telefone no formato: +551140028922'))

phone_number = parse(phone)

print(geocoder.description_for_number(phone_number, 'pt'))
