
#taken from this StackOverflow answer: https://stackoverflow.com/a/39225039
import requests
import argparse

def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)


def parse_args():
    """Parse command line arguments.
    """
    parser = argparse.ArgumentParser(description="downloader")
    parser.add_argument(
        "--deep_sort_path",
        help="Path the deep_sort repository.",
        required=True)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    print("weight for deep_sort download")
    print("1/17")
    download_file_from_google_drive('19zDNCQoQi3hITTO77DLCp6KmefVNpf1D', args.deep_sort_path+'/resources/networks/mars-small128.pb')
    print("2/17")
    download_file_from_google_drive('1Ha525g-BBPo7RitlpgfaXPDzm8NHRPum', args.deep_sort_path+'/resources/networks/mars-small128.ckpt-68577.meta')
    print("3/17")
    download_file_from_google_drive('17HIeHPmdKHB2sgLo_Eqm5iYjkv3NkaVQ', args.deep_sort_path+'/resources/networks/mars-small128.ckpt-68577')
    print("4/17")
    download_file_from_google_drive('1s1pgb1ZivoRv_dhB4hHSpR5BcBu1KAHr', args.deep_sort_path+'/resources/detections/MOT16_POI_train/MOT16-13.npy')
    print("5/17")
    download_file_from_google_drive('19xPvuyHmCi8eXoMdHCSv2tSvKs2divF5', args.deep_sort_path+'/resources/detections/MOT16_POI_train/MOT16-11.npy')
    print("6/17")
    download_file_from_google_drive('1zaZLeWjkJOfCT53Pehr0rbNp1LFyZu6g', args.deep_sort_path+'/resources/detections/MOT16_POI_train/MOT16-10.npy')
    print("7/17")
    download_file_from_google_drive('1zaZLeWjkJOfCT53Pehr0rbNp1LFyZu6g', args.deep_sort_path+'/resources/detections/MOT16_POI_train/MOT16-09.npy')
    print("8/17")
    download_file_from_google_drive('1yIMBSdHvpPT8EY0czD1azQ8lrn471SAO', args.deep_sort_path+'/resources/detections/MOT16_POI_train/MOT16-05.npy')
    print("9/17")
    download_file_from_google_drive('1QsGVtGZ5ktkTVenGNrl1xOIafDlXyiXQ', args.deep_sort_path+'/resources/detections/MOT16_POI_train/MOT16-04.npy')
    print("10/17")
    download_file_from_google_drive('1QsGVtGZ5ktkTVenGNrl1xOIafDlXyiXQ', args.deep_sort_path+'/resources/detections/MOT16_POI_train/MOT16-02.npy')
    print("11/17")
    download_file_from_google_drive('1G3BEexcelln723tzC5vhisGMMZVxEXKA', args.deep_sort_path+'/resources/detections/MOT16_POI_test/MOT16-14.npy')
    print("12/17")
    download_file_from_google_drive('1mRCdJ8WKQwb_ZdQO6VMR00uV9KDUwEHV', args.deep_sort_path+'/resources/detections/MOT16_POI_test/MOT16-12.npy')
    print("13/17")
    download_file_from_google_drive('1jrgiGYczEeeA5wH7wTN-pbJAqdKGPx-W', args.deep_sort_path+'/resources/detections/MOT16_POI_test/MOT16-08.npy')
    print("14/17")
    download_file_from_google_drive('1aryMbn5I_sfHNgYTOA_AraBupaowzJcP', args.deep_sort_path+'/resources/detections/MOT16_POI_test/MOT16-07.npy')
    print("15/17")
    download_file_from_google_drive('1rFI9EIluSzFiUxj_NcRU_5Hju7A87DST', args.deep_sort_path+'/resources/detections/MOT16_POI_test/MOT16-06.npy')
    print("16/17")
    download_file_from_google_drive('1aKRnBn-LrSrNsZbQvvSSQVhVY_13PL30', args.deep_sort_path+'/resources/detections/MOT16_POI_test/MOT16-03.npy')
    print("17/17")
    download_file_from_google_drive('164AWlR6zr-zlrHbfNxOlz-h-a5yiacl9', args.deep_sort_path+'/resources/detections/MOT16_POI_test/MOT16-01.npy')
