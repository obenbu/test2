#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np

def nothing(x):
    pass

def main():
    video_input = cv2.VideoCapture(0)

    # ガンマ値設定用のトラックバー用意(小数点を扱えないため、10倍の値で準備)
    cv2.namedWindow("gammma correction", cv2.WINDOW_NORMAL)
    cv2.createTrackbar("gamma(0.1)", "gammma correction", 1, 50, nothing)
    cv2.setTrackbarPos("gamma(0.1)", "gammma correction", 10)

    while(1):
        ret, frame = video_input.read()

        # ガンマ値取得（0は強制的に0.1相当に引き戻し）
        gamma = cv2.getTrackbarPos("gamma(0.1)", "gammma correction") * 0.1
        if gamma == 0:
            gamma = 0.1
            cv2.setTrackbarPos("gamma(0.1)", "gammma correction", 1)

        # ガンマ補正用ルックアップテーブル
        look_up_table = np.zeros((256, 1), dtype = 'uint8')
        for i in range(len(look_up_table)):
            look_up_table[i][0] = (len(look_up_table)-1) * pow(float(i) / (len(look_up_table)-1), 1.0 / gamma)

        # ルックアップテーブルによるガンマ補正
        gamma_correction_image = cv2.LUT(frame, look_up_table)

        # ウィンドウ表示
        cv2.putText(gamma_correction_image, "gamma:" + str(gamma), (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0,0,0),2)
        cv2.imshow("gammma correction", gamma_correction_image)

        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    video_input.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
