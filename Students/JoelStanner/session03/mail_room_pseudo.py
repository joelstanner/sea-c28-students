while user_input != "Quit"

    def get_user_input(prompt, validator=None):
        """request input from the user with `prompt` and return the result.

        optionally, validate the input with a function `validator` which must
        take one argument, the input from the user and must return the input if
        valid, and None if not valid
        """
        reply = None
        while reply is None:
            reply = ask_for_input(prompt)
            if there_is_a_validator:
                validate_the_reply
        return reply


    def thank_report_quit():
        """Prompt the user for an action.

        Valid choices are:
        Thank you note
        donor report
        quit
        """
        user_input = get_user_input("Thank, Report, or Quit?", 
                                    validator=valid_input)
        if user_input == "Thank":
            get_user_input("Enter a full name or 'list' for a list of donors",
                            validator=valid_input)
            if reply == "list":
                print_list_of_donors()
                thank_report_quit()
            elif reply == name_not_in_list:
                add_name_to_data_structure
                donation_amount()

        donation_amount()

        elif user_input == "Report":
        print(donor_name, total_donated, number_of_donations, avg_donation_amt)
        return to prompt

def donation_amount():
    donation = get_user_input("how much is the donation?", validator=validator)
    add_donation_to_donation_history
    print(thank_you_email)
    return to prompt

