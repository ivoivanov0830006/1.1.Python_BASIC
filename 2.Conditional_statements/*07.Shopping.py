budget = float(input())
video_count = int(input())
processor_count = int(input())
memory_count = int(input())

video_price = 250
total_video = video_count * video_price
processor_price = 0.35 * total_video
total_processor = processor_count * processor_price
memory_price = 0.1 * total_video
total_memory = memory_count * memory_price
spent = total_video + total_processor + total_memory
diff = 0
if video_count > processor_count:
    spent = spent - (spent * 0.15)
    if budget >= spent:
        diff = abs(budget - spent)
        print(f"You have {diff:.2f} leva left!")
    else:
        diff = abs(budget - spent)
        print(f"Not enough money! You need {diff:.2f} leva more!")
else:
    if budget >= spent:
        diff = abs(budget - spent)
        print(f"You have {diff:.2f} leva left!")
    else:
        diff = abs(budget - spent)
        print(f"Not enough money! You need {diff:.2f} leva more!")
        
        
# ------------------------------ Another Solution ----------------------------
#
# budget = float(input())
# video_count = int(input())
# processor_count = int(input())
# memory_count = int(input())
#
# video_price = 250
# total_video = video_count * video_price
# processor_price = 0.35 * total_video
# total_processor = processor_count * processor_price
# memory_price = 0.1 * total_video
# total_memory = memory_count * memory_price
# spent = total_video + total_processor + total_memory
#
# if video_count > processor_count:
#     spent = spent - (spent * 0.15)
#
# diff = abs(budget - spent)
# if budget >= spent:
#     print(f"You have {diff:.2f} leva left!")
# else:
#     print(f"Not enough money! You need {diff:.2f} leva more!")
