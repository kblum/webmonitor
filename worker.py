from crash_hound import CrashHound, CommonChecks, SenderMail

# helper lambda for gracefully degrading environmental variables
from os import environ
env = lambda e, d: environ[e] if environ.has_key(e) else d

# load configuration from environment variables
monitor_url = env('MONITOR_URL', '')
smtp_host = env('SMTP_HOST', '')
smtp_user = env('SMTP_USER', '')
smtp_password = env('SMTP_PASSWORD', '')
email_to = env('EMAIL_TO', '')

crash_sender = SenderMail(email_to, email_to, smtp_host, smtp_user, smtp_password)

crash_checker = CrashHound(crash_sender)

# check URL and send notifications if it does not return a status of 200 or 302
message_subject = '[Webmonitor] {0} Status Check'.format(monitor_url)
crash_checker.register_check(message_subject, 
    lambda: CommonChecks.website_check(monitor_url), notify_every=60*60)

# run checks every 30 minutes (indefinitely)
crash_checker.run_checks(check_interval=30*60)
