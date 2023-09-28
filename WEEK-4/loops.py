# Loops: for and while loop
# The purpose of loop is to avoid repetion or to solve repetive problem
# 0 to 100

# print(list(range(0, 101)))

""" for i in range(0, 11):
    print(i) """

nums = [1, 2, 3]

for num in nums:
    pass
    # print(num, num * num, num ** 3)

countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']

new_lst = []
for country in countries:
    new_lst.append([country, country.upper(),
                   country.upper()[:3], len(country)])
    # print(country, country.upper(), country.upper()[0:3], len(country))
# print(new_lst)

""" nums = []
for i in range(0, 101):
    nums.append([i, i ** 2, i ** 3])
print(nums) """


names = ['Zarin', 'Markku', 'Pawan', 'Almir', 'Sonja', 'Kalle', 'Elina']


for name in names:
    message = f'''
    Hello {name}

    The Python lesson is going to be started by 17:30. I would like you to be around by 17:25.

    Kind regards,
    Asabeneh
    '''
    print(message)


'single'
"double quote"
txt = ''' or you triple quote to make string'''
abc = """
djdjdjdjd
"""

# To sum up from zero to 100, how to you sum these up

total = 0
for i in range(0, 101):
    # total = total + i
    total += i
# print(total)

# continue and break

nums = [3, 1, 5, -4, 6, 8]

for num in nums:
    if num < 0:
        continue
    # print(num)
    
    
for num in nums:
    if num < 0:
        continue
    # print(num)


    
for num in nums:
    if num < 0:
        break
    print(num)
    
    
    

countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
countries_with_land = []

for country in countries:
    if 'land' in country:
        countries_with_land.append(country)
print(countries_with_land)

countries_with_den = []

for country in countries:
    if 'den' in country.lower():
        countries_with_den.append(country)
print(countries_with_den)


countries_without_land = []

for country in countries:
    if 'land' not in country:
        countries_without_land.append(country)
print(countries_without_land)

# a ** 3 = a * a * a
# a ** 2 = a * a
# a ** 10
for i in range(0, 11):
    print(f'{i} x {i} = {i ** i}')
    
    
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
""" for i in range(len(countries)):
    print(i, countries[i]) """
    
""" countries_copied = countries.copy()
countries_copied.reverse()
for country in countries_copied:
    print(country) """
    
# 0, 2, 3,4 => 4, 3, 2, 1, 0
print(list(range(4, -1, -1)))
last_index = len(countries)- 1
for i in range(last_index, -1, -1):
    print(countries[i])
    
    
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

countries_with_land = []

for country in countries:
    if 'land' in country:
        countries_with_land.append(country)
        
print(countries_with_land, len(countries_with_land))

countries_with_two_words = []

for country in countries:
    words = country.split(' ')
    if len(words) >= 2:
        countries_with_two_words.append(country)
        
print(countries_with_two_words)