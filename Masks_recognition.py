import cv2
import os
import dlib
import tensorflow as tf
from glob import glob
from xml.dom.minidom import parse

images_list = sorted(glob('./masks/images/*.png'))
color_list = ((255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255))


class ParsedImage:
    def __init__(self, file_name):
        self.file_name = file_name
        self.image = None
        self.shape = None
        try:
            file_path = os.path.join('./masks/images', file_name)
            if os.path.isfile(file_path) and file_path in images_list:
                self.image = cv2.imread(file_path)
                self.shape = self.image.shape
        except Exception as e:
            print(f'File {file_name} does not exist')
            print(e)
        self.objects = []

    def add_object(self, human_object):
        self.objects.append(human_object)

    def get_faces(self, show_flag=False):
        faces_list = []
        for i, hf in enumerate(self.objects):
            face_img = self.image[hf.bbox[1]: hf.bbox[3], hf.bbox[0]: hf.bbox[2], :]
            face_img = cv2.cvtColor(face_img, cv2.COLOR_RGB2GRAY)
            face_img = cv2.resize(face_img, (30, 44))
            faces_list.append((face_img, int(hf.mask)))
            if show_flag:
                cv2.imshow(str(i), face_img)
        if show_flag:
            cv2.waitKey(0)
        return faces_list

    def detect_face(self):
        gray = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)
        detector = dlib.get_frontal_face_detector()
        dets = detector(gray, 3)
        print("Number of faces detected: {}".format(len(dets)))
        for i, d in enumerate(dets):
            print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
                i, d.left(), d.top(), d.right(), d.bottom()))
            x, y = int((d.right() + d.left()) / 2), int((d.top() + d.bottom()) / 2)
            h, w = int((d.right() - d.left())), int((d.bottom() - d.top()) / 2)
            gray = cv2.ellipse(gray, (x, y), (w, h), 0, 0, 360, (255, 0, 255), 4)
        cv2.imshow('face', gray)
        cv2.waitKey(0)

    # def detect_face_haar_cv2(self):
    #     gray = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)
    #     gray = cv2.equalizeHist(gray)
    #     face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    #     eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    #     faces = face_cascade.detectMultiScale(gray)
    #     for (x, y, w, h) in faces:
    #         center = (x + w // 2, y + h // 2)
    #         frame = cv2.ellipse(gray, center, (w // 2, h // 2), 0, 0, 360, (255, 0, 255), 4)
    #         faceROI = gray[y:y + h, x:x + w]
    #         # -- In each face, detect eyes
    #         eyes = eye_cascade.detectMultiScale(faceROI)
    #         for (x2, y2, w2, h2) in eyes:
    #             eye_center = (x + x2 + w2 // 2, y + y2 + h2 // 2)
    #             radius = int(round((w2 + h2) * 0.25))
    #             frame = cv2.circle(frame, eye_center, radius, (255, 0, 0), 4)
    #     cv2.imshow('face', gray)

    def show_image(self):
        if self.image is not None:
            img = self.image.copy()
            for i, human_face in enumerate(self.objects):
                img = human_face.draw_me(img, color_list[i % 6])
            cv2.imshow(self.file_name, img)
            cv2.waitKey(0)


class HumanFace:
    def __init__(self, mask, bbox, pose='Unspecified', difficult=0, occluded=0):
        self.mask = False if 'without_mask' in mask else True
        self.bbox = bbox
        self.pose = pose
        self.difficult = difficult
        self.occluded = occluded

    def draw_me(self, image, color):
        if self.mask:
            image = cv2.line(image, (self.bbox[0], self.bbox[1]), (self.bbox[2], self.bbox[3]), color=color)
            image = cv2.line(image, (self.bbox[2], self.bbox[1]), (self.bbox[0], self.bbox[3]), color=color)
        return cv2.rectangle(image, (self.bbox[0], self.bbox[1]), (self.bbox[2], self.bbox[3]), color=color,
                             thickness=1)


def get_image_list(annotations_list, number=-1):
    image_list = []
    if number > len(annotations_list):
        number = -1
    for annotation_file in annotations_list[:number]:
        with open(annotation_file) as xml_file:
            print(f'Reading file {annotation_file}')
            dom_document = parse(xml_file)  # parse an open file
            image_name = str(dom_document.getElementsByTagName('filename')[0].firstChild.nodeValue)
            parsed_image = ParsedImage(image_name)

            for object_element in dom_document.getElementsByTagName('object'):
                object_name = object_element.getElementsByTagName('name')[0].firstChild.nodeValue
                object_bbox = []
                bbox_element = object_element.getElementsByTagName('bndbox')[0]
                for el_name in ['xmin', 'ymin', 'xmax', 'ymax']:
                    object_bbox.append(int(bbox_element.getElementsByTagName(el_name)[0].firstChild.nodeValue))
                parsed_image.add_object(HumanFace(object_name, tuple(object_bbox)))
            image_list.append(parsed_image)
    return image_list


if __name__ == '__main__':
    image_size = (30, 44)
    annotations_list = sorted(glob('./masks/annotations/*.xml'))
    image_list = get_image_list(annotations_list)
    faces_list = []
    for img in image_list:
        faces_list.extend(img.get_faces())
    inputs, targets = zip(*faces_list)

