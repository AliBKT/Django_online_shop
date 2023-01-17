from django import template

register = template.Library()

@register.filter
def translate_number_english_to_persion(number) :
    number = str(number)
    english_to_persion_table = number.maketrans("9876543210","٩٨٧٦٥٤٣٢١۰")
    return number.translate(english_to_persion_table)
    
@register.filter
def commaint(number):
    number = str(number)
    for i in range(len(number)-3,0,-3):
        number = number[0:i]+','+number[i:len(number)]
    return number
