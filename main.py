from icalendar import Calendar, Event
from datetime import datetime


def generate_ics_file(
    prodid: str,
    version: str,
    uid: str,
    summary: str,
    dtstart: datetime,
    dtend: datetime,
    description: str,
    location: str,
):
    cal = Calendar()
    cal.add("prodid", prodid)
    cal.add("version", version)

    event = Event()
    event.add("uid", uid)
    event.add("summary", summary)
    event.add("dtstart", dtstart)
    event.add("dtend", dtend)
    event.add("description", description)
    event.add("location", location)

    cal.add_component(event)

    with open("sample.ics", "wb") as f:
        f.write(cal.to_ical())


def generate_google_calendar_link(
    event_title, start_time, end_time, location, description
):
    # Format the datetime objects to the required format for Google Calendar
    start_time_str = start_time.strftime("%Y%m%dT%H%M%S")
    end_time_str = end_time.strftime("%Y%m%dT%H%M%S")

    # Construct the Google Calendar link
    google_calendar_link = (
        f"https://www.google.com/calendar/render?action=TEMPLATE&text={event_title}"
        f"&dates={start_time_str}/{end_time_str}&details={description}&location={location}"
    )

    return google_calendar_link


# Example usage:
event_title = "Sample Event"
start_time = datetime(2023, 1, 1, 10, 0, 0)  # Replace with your start time
end_time = datetime(2023, 1, 1, 12, 0, 0)  # Replace with your end time
location = "Sample Location"
description = "This is a sample event description."

google_calendar_link = generate_google_calendar_link(
    event_title, start_time, end_time, location, description
)

print(f"Google Calendar Link: {google_calendar_link}")
