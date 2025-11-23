total_seconds = int(input("Введите количество секунд: "))

minutes = total_seconds // 60 
seconds = total_seconds % 60   

print(str(total_seconds) + " секунд(ы) = " + str(minutes) + " минута(ы) " + str(seconds) + " секунд(ы)")