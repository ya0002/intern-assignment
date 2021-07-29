import xml.etree.ElementTree as ET 
import cv2
import os


def draw_rectangles(o, img):
    bbs = o.find('bndbox')
    xmin = float(bbs.findtext("xmin"))
    ymin = float(bbs.findtext("ymin"))
    xmax = float(bbs.findtext("xmax"))
    ymax = float(bbs.findtext("ymax"))
    s_point = (int(xmin), int(ymin))
    e_point = (int(xmax), int(ymax))
    img = cv2.rectangle(img, s_point, e_point, (0, 0, 255), 2)
    return img, xmin, ymin


def write_label(o, img, xmin, ymin):
    state = o.find('name').text
    cv2.putText(img, state, (int(xmin)-20, int(ymin)-5),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    return img


def save_img(root, img_file, img, dir_name='Results'):
    try:
        os.makedirs(os.path.join(root, dir_name))
    except:
        pass
    new_img_name = os.path.join(root, dir_name, img_file)
    cv2.imwrite(new_img_name, img)


def draw_bb(root, img_files, to_save_dir):
    for img_file in img_files:

        img_root = os.path.join(root, img_file)
        img = cv2.imread(img_root)

        try:
            xml_root = f'{img_root[:-3]}xml'
            parser = ET.parse(xml_root).getroot()
            objects = parser.findall('object')

            for o in objects:
                try:
                    img, xmin, ymin = draw_rectangles(o, img)
                    img = write_label(o, img, xmin, ymin)
                except:
                    pass
            save_img(root, img_file, img, dir_name=to_save_dir)
            print(f'results saved for {img_file} to {to_save_dir}')
        except:
            print(f'NO results saved for {img_file}')
            pass


if __name__ == '__main__':
    root = 'D:\yusuf\Downloads\Internships\Traffic Light\intern-assignment'
    to_save_dir_name = 'Result-4'
    img_files = [i for i in os.listdir(root) if i.endswith('png') or i.endswith('.jpg')]
    draw_bb(root, img_files, to_save_dir_name)
