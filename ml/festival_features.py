def get_festival_flag(month):
      festival_months = {
            1: 1,   # Makar Sankranti
            3: 1,   # Holi
            8: 1,   # Raksha Bandhan
            10: 1,  # Diwali
            11: 1,  # Wedding season
            12: 1   # Christmas
      }

      return festival_months.get(month, 0)


def get_season(month):
      if month in [12, 1, 2]:
            return 1   # Winter
      elif month in [3, 4, 5]:
            return 2   # Summer
      elif month in [6, 7, 8, 9]:
            return 3   # Rainy
      else:
            return 4   # Festival/autumn