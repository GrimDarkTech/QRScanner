import cv2

def main():
    # Открываем вебкамеру (0 - это индекс камеры, может быть 1, 2 и т.д. для других камер)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Не удалось открыть вебкамеру")
        return

    while True:
        # Читаем кадр из вебкамеры
        ret, frame = cap.read()
        if not ret:
            print("Не удалось получить кадр")
            break

        # Создаем объект для декодирования QR-кодов
        detector = cv2.QRCodeDetector()

        # Декодируем QR-код
        data, points, _ = detector.detectAndDecode(frame)

        # Если QR-код распознан
        if data:
            # Отображаем информацию о QR-коде
            print(f"QR-код распознан: {data}")

            # Рисуем рамку вокруг QR-кода
            if points is not None:
                    frame = cv2.polylines(frame, points.astype(int), True, (0, 255, 0), 3)

        # Отображаем изображение
        cv2.imshow('QR Code Scanner', frame)

        # Выход из цикла при нажатии клавиши 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Освобождаем ресурсы
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
