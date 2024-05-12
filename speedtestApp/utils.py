import speedtest
import urllib.request
import time

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

def measure_speed(url, file_size):
    time_start = time.time()
    response = urllib.request.urlopen(url)
    downloaded_bytes = 0
    while True:
        data_chunk = response.read(1024) 
        if not data_chunk:
            break
        downloaded_bytes += len(data_chunk)
    time_end = time.time()
    print(f'Downloaded {downloaded_bytes} bytes in {time_end - time_start} seconds')
    download_speed = (downloaded_bytes * 8) / (time_end - time_start) / 1024 / 1024  
    return download_speed  