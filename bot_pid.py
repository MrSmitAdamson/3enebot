def bot_pid_file_write_func(pid):
    open('pid', 'w').close()
    f = open('pid', 'w')
    f.write(pid)
    f.close()