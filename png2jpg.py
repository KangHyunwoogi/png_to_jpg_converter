import os
from PIL import Image

# 변환할 PNG 이미지가 있는 폴더 경로
input_folder = "/home/ailab/wook/bag_deliver_B"

# 변환된 JPG 이미지를 저장할 폴더 경로
output_folder = "/home/ailab/wook/deliver_jpg"

# PNG 이미지를 JPG로 변환하는 함수
def convert_png_to_jpg(input_path, output_folder, count):
    count=count+433
    try:
        # PNG 이미지 열기
        image = Image.open(input_path)

        # JPG로 저장
        output_filename = f"{count:06d}.jpg"
        output_path = os.path.join(output_folder, output_filename)
        image.save(output_path, "JPEG")

        # 이미지 닫기
        image.close()

        print(f"{input_path}를 {output_filename}로 변환했습니다.")
    except Exception as e:
        print(f"변환 중 오류 발생: {e}")

# 입력 폴더 내의 모든 파일 목록 얻기
png_files = [filename for filename in os.listdir(input_folder) if filename.endswith(".png")]
png_files = sorted(png_files)

# PNG 파일을 순서대로 읽어와서 JPG로 변환하여 저장
for count, png_filename in enumerate(png_files):
    
    input_path = os.path.join(input_folder, png_filename)
    convert_png_to_jpg(input_path, output_folder, count)