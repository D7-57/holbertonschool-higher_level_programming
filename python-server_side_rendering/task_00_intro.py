def generate_invitations(template_content, attendees):
    if(not template_content or not (isinstance(template_content, string))):
        raise EXCEPTION("the template is must be a string")
    if((not (isinstance(attendees, list))) and not (all(isinstance(item, dict) for item in attendees))):
        raise EXCEPTION("the attendees must be a list full of dictionaries")


    count = 0
    for attendent in attendees:
        name = attendent.get("name", "N/A")
        event_title = attendent.get("event_title", "N/A")
        event_date = attendent.get("event_date", "N/A")
        event_location = attendent.get("event_location", "N/A")
    
        template = template_content
        template.replace("\{name\}",name)
        template.replace("\{event_title\}",event_title)
        template.replace("\{event_date\}",event_date)
        template.replace("\{event_location\}",event_location)

        outputOG = "output_X.txt"
        count += 1
        outputOG.replace("X", str(count))
        with open(outputOG, 'w') as file:
            file.write(template)


with open('template.txt', 'r') as file:
    template_content = file.read()

# List of attendees
attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]

# Call the function with the template and attendees list
generate_invitations(template_content, attendees)





