#!/usr/bin/env python

"""This is Mailroom Madness"""

def promt_full_name(directory):
    """Promt user for full name and check if its in the directory


    if name exists - select it. Else add the new name. Once name is identified 
    calls promt_donation_ammount and assigns value of donation"""
    full_name = raw_input("please enter the full name with a space or ask for a list of donors ")
    full_name.lower()
    if full_name == "list":
        print directory
        return promt_full_name(directory)
    else:
        #name = full_name.split() - use this to break into first and last names
        get_vale = promt_donation_ammount()
        directory.setdefault(full_name, get_vale)
        letter = u"""Thank you {name} for your generous donation of {donation_amount} dollars
        """
        print letter.format(name=full_name, donation_amount=get_vale)

        return directory


def promt_donation_ammount():
    """Promt user to enter the donation for a previsouly selected name"""


    donation = raw_input("Please enter the ammount donated as numbers ")
    if donation.isdigit():
        return donation
    else:
        print "Thats not quite right - try again"
        return promt_donation_ammount()

def report(directory):
    "Ceate and format a report - Printed to the user"


    new_list = []
    for i in directory.iterkeys():
        total = directory.get(i)
        number = sum(total)
        average = number / len(total)
        new_list.append([i, number, average])
    new_list.sort()
    report_text = u"Name      Total Donation        Average Donation"
    print report_text
    for y in new_list:
        print u"{:<18} {:^18} {:>18}".format(y[0], y[1], y[2])



if __name__ == '__main__':
    directory_of_names = {'allen' : (200, 100, 250), 'Paul' : (50, 20, 30), 'Max Green' : (1000, ),
                          'Jake Chesterfield' : (3445, 31, 777), 'Eric Abelman' : (123456,)}


    def main_selection(dirctory):
        """Promt the user to selecte report or thanks you note"""
        while True:
            try:
                main_input = raw_input("Options: Thank You - t , Report - r , Quit - q ")
                main_input.lower()
            except (EOFError, KeyboardInterrupt):
                print "\ntry again\n"
            else:
                if main_input == 't':
                    promt_full_name(dirctory)
                elif main_input == 'r':
                    report(dirctory)
                elif main_input == 'q':
                    break
                else:
                    print "try again"


    main_selection(directory_of_names)
