import storage
import supervisor

# Disable write protection (must be in boot.py)
storage.remount("/", readonly=False)
supervisor.runtime.autoreload = False
