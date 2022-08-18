def imageProcessing(img, input_shape, tracker):
  markers = tracker.processFrame(img)

  # Обработка положения маркеров

  # возврат результата
  # тип цели, курс на цель, угол цели, расстояние 
  # или
  # None