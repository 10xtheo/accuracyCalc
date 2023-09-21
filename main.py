# input section started 
print("Введите число измерений N: ")
N = int(input())
measurments = []
print("Введите N измерений, отправляя каждое с помощью ENTER: ")
for i in range(N):
    measurments.append(int(input()))
print("Введите цену деления на приборе: ")
partition= int(input())
# input section ended
measurments = sorted(measurments)
N = len(measurments)
scope = abs(measurments[4] - measurments[0]) # найдем размах
U95coma5 = 0.64 # U коэфициент 
# проверка на промахи
if (abs(measurments[0] - measurments[1]) >= U95coma5*scope) or (abs(measurments[4] - measurments[3]) >= U95coma5*scope):
    print("Ошибка на этапе проверки на промахи")
median = sum(measurments) / N # найдем среднее
# найдем СКО
numerator = 0
for i in range(N):
    numerator += (measurments[i] - median)**2
sqDevitation = (numerator/(N - 1))**0.5

averageSqDevitation = sqDevitation / N**0.5 # найдем ско среднего

# найдем случайную погрешность
beta95coma5 = 0.51 # бета коэфициент
randomAccuracyScope = beta95coma5*scope  # по размаху
t95coma5 = 2.8 # t коэфициент
randomAccuracyAverageSqDevitation = t95coma5*averageSqDevitation # по ско
randomAccuracy = max(randomAccuracyAverageSqDevitation, randomAccuracyScope) # выберем наибольшую случайную погрешность
instrumentAccuracy = partition/2 # найдем приборную погрешность
fullAccuracy = (randomAccuracy**2 + instrumentAccuracy**2)**0.5 # найдем полную погрешность
relativeAccuracy = (fullAccuracy/median) * 100 # найдем относительную погрешность
print("Относительная погрешность = ", relativeAccuracy, "%")
print("Ответ: ", median, '±', fullAccuracy)
print("Ответ округлите по правилам округления.")
