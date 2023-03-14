kata = (2019, 9, 25, 3, 30)

formatted_date = f"{str(kata[1]).zfill(2)}/{str(kata[2]).zfill(2)}/{kata[0]}"
formatted_time = f"{str(kata[3]).zfill(2)}:{str(kata[4]).zfill(2)}"

print(f"{formatted_date} {formatted_time}")