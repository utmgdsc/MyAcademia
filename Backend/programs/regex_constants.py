import re

# For different types of categories for helping in quering the database

# For Course Code followed by a hypen then a +: E.g- WGS-300+
courseCodePlusRe = re.compile('[A-Z]{3}-[0-9]{3}\+')
# For program-title E.g-ER_SOC3
programTitleRe = re.compile('ER_[A-Z]{3}[0-9]{1,3}')
#For courses type: E.g SOC-COURSES
courseTypeRe = re.compile('[A-Z]{3}-COURSES')
#For courses Code without a plus:E.g-MAT-400
courseCodeRe = re.compile('[A-Z]{3}-[0-9]{3}')
