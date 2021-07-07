import threading

import main_window



winThread=threading.Thread(main_window.main())
winThread.start()