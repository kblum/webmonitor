# Website Status Monitor

This project is a small worker application that uses a [fork](https://github.com/kblum/crash_hound) of the [Crash Hound](https://github.com/Doist/crash_hound) Python library to monitor a website and send an email notification using a specified SMTP server if the website stops responding correctly. If the monitored URL does not return a status code of 200 or 302 it is assumed to be down. The application monitors a specified URL.

The worker application will check the status of the target URL every 30 minutes and will send an email notification every 60 minutes if an incorrect status code is returned.

## Dependencies

The project should be set up in a `virtualenv`. The dependencies can then be installed using `pip`:

	pip install -r requirements.txt

## Configuration

All application configured is managed using environment variables.

The URL to monitor, notification email address as well as the credentials for the SMTP must be set as environment variables. The `EMAIL_TO` variable will be used for both the destination and source email addresses.

* `MONITOR_URL` - website URL to monitor the status of.
* `EMAIL_TO` - source and destination email address for notifications.
* `SMTP_HOST`- IP address or hostname of the SMTP server.
* `SMTP_USER` - user to authenticate the SMTP connection with.
* `SMTP_PASSWORD`- password to authenticate the SMTP connection with.

Port 587 is used for the SMTP connection and traffic is encrypted using TLS.

## Deployment

The monitor application can be deployed to [Heroku](http://heroku.com) as a Python worker (remembering to set the appropriate environment variables):

	heroku ps:scale web=0
	heroku ps:scale worker=1
