# speedtest/utils.py
import speedtest

def run_speed_test():
    st = speedtest.Speedtest()
    download_speed = st.download() / 1024 / 1024 
    upload_speed = st.upload() / 1024 / 1024  
    ping = st.results.ping

    return {
        'download_speed': download_speed,
        'upload_speed': upload_speed,
        'ping': ping
    }
