# Cartoon_Jeans
New Jeans OMG photo to cartoon using image processing
OpenCV 라이브러리 함수를 이용하여 입력 이미지('OMG.jpg')에 대해 다양한 이미지 처리 기법을 수행하고 결과 이미지를 표시하는 코드입니다.

### 0. Original
<img width="638" alt="new1" src="https://user-images.githubusercontent.com/113033780/227871469-b8de7451-613c-4c5c-a590-210b2bd32fb2.png">

### 1. Cartoonization
이 기술은 입력 이미지를 회색조로 변환하고, 가우시안 블러를 적용하고, 적응 임계값을 사용하여 가장자리 감지를 수행하고, 가장자리를 양면 필터링된 컬러 이미지와 결합하여 만화 같은 효과를 생성합니다. 결과 이미지는 '만화'에 저장됩니다.
<img width="638" alt="new2" src="https://user-images.githubusercontent.com/113033780/227871857-0c951959-03a1-41ef-adf6-40327f5ab043.png">

### 2. Color Quantization Filter
이 기술은 전체 모양을 유지하면서 이미지에 사용되는 색상 수를 줄입니다. k-평균 클러스터링을 사용하여 유사한 색상을 함께 그룹화하고 더 작은 대표 색상 세트에 매핑합니다. 결과 이미지는 'res2'에 저장됩니다.
<img width="959" alt="new4" src="https://user-images.githubusercontent.com/113033780/227871967-39e4b9b6-3e37-40e0-b1df-e5d3f98c643c.png">

### 3. Pencil Sketch Filter
이 기술은 입력 이미지를 회색조로 변환하고 연필 스케치 효과를 적용합니다. 이는 종이에 연필로 그리는 효과를 시뮬레이트하는 OpenCV의 'pencilSketch' 함수를 사용하여 수행됩니다. 결과 이미지는 'pencil_sketch_img'에 저장됩니다.
<img width="953" alt="new3" src="https://user-images.githubusercontent.com/113033780/227871924-9c41b8ba-003c-4dc7-bf68-4aef690f840f.png">

### 4. Bilateral + Median + Stylization Filter
이 기술은 필터 조합을 이미지에 적용하여 가장자리를 향상시키고 만화 효과를 생성합니다. 첫째, 가장자리를 유지하면서 이미지를 부드럽게 하기 위해 양방향 필터가 적용됩니다. 그런 다음 중앙값 필터를 적용하여 잡음을 제거하고 가장자리를 보존합니다. 마지막으로 가장자리를 향상시키고 만화 효과를 생성하기 위해 스타일화 필터가 적용됩니다. 결과 이미지는 'stylized'에 저장됩니다.
<img width="957" alt="new5" src="https://user-images.githubusercontent.com/113033780/227872019-67fddae4-29cb-46e8-b1c3-7b7a4a6fc93b.png">

결과 이미지는 'cv2.imshow' 함수를 사용하여 표시됩니다. 위에서 설명한 네 가지 이미지 처리 기술의 출력 이미지와 함께 원본 이미지가 표시됩니다. 
