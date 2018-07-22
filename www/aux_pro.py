import os
import signal
import subprocess

class Process(object):
    process = None
    def start_process(self, d_m, id_match):
        if self.process == None:
            cmd = "python3 process.py %s %s %s" % (d_m["team1"], d_m["team2"], id_match)
            self.process = subprocess.Popen(cmd.split(), preexec_fn=os.setsid)
            return self.process.pid
        return None
    
    def stop_process(self):
        if self.process != None:
            os.killpg(os.getpgid(self.process.pid), signal.SIGTERM)
            self.process = None
    