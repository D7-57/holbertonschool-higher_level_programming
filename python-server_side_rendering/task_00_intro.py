def generate_invitations(template_content, attendees):
    # Check if template_content is a string
    if not template_content or not isinstance(template_content, str):
        print("Error: Template must be a non-empty string.")
        return

    # Check if attendees is a list of dictionaries
    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Check if the template is empty
    if not template_content.strip():
        print("Error: Template is empty, no output files generated.")
        return

    # Check if the list of attendees is empty
    if not attendees:
        print("Error: No data provided, no output files generated.")
        return

    # Process each attendee and create output files
    count = 0
    for attendee in attendees:
        # Replace missing data with "N/A"
        name = attendee.get("name", "N/A")
        event_title = attendee.get("event_title", "N/A")
        event_date = attendee.get("event_date", "N/A")
        event_location = attendee.get("event_location", "N/A")

        # Create a copy of the template and perform replacements
        template = template_content
        template = template.replace("{name}", name)
        template = template.replace("{event_title}", event_title)
        template = template.replace("{event_date}", event_date)
        template = template.replace("{event_location}", event_location)

        # Create output file name dynamically
        count += 1
        output_file = f"output_{count}.txt"

        # Write the personalized invitation to the output file
        with open(output_file, 'w') as file:
            file.write(template)
        print(f"Invitation for {name} written to {output_file}")
