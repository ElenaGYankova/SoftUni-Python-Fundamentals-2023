import re

pattern = r'^(\$([A-Z][a-z]{2,})\$|\%([A-Z][a-z]{2,})\%): (\[\d+\]\|\[\d+\]\|\[\d+\]\|)$'
number_of_messages = int(input())
