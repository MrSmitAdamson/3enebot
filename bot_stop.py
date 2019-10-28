
import admins

import bot_report

def stop_func(admin):
    if admins.admin_check(admin):
        bot_report.bot_stopped_message_func(admin)
        raise SystemExit
 
   

