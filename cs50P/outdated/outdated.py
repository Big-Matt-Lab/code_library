"""
CS50 Outdated date format converter
"""

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def is_valid_date(year, month, day):
    """
    Checks for a valid date,
    """
    if not (1 <= month <= 12):
        return False

    # Day must be between 1 and 31
    if not (1 <= day <= 31):
        return False

    return True


def main():
    """ Main program loop"""
    while True:
        try:
            date_input = input("Date: ").strip()

            if not date_input:  # Exit on no input
                break

            # Initialize date
            year, month, day = None, None, None

            # MM/DD/YYYY format
            if "/" in date_input:
                try:
                    m_str, d_str, y_str = date_input.split('/')
                    # Convert to ints
                    m, d, y = int(m_str), int(d_str), int(y_str)
                    if is_valid_date(y, m, d):
                        year, month, day = y, m, d
                except ValueError:
                    pass  # Failed, try another way

            # month day, year format
            if year is None and "," in date_input:
                try:
                    # Remove comma
                    parts = date_input.replace(",", "").split()
                    if len(parts) == 3:
                        month_name, d_str, y_str = parts
                        # Get month index, accounting for 'may' vs 'May'
                        if month_name.title() in months:
                            m = months.index(month_name) + 1
                            d = int(d_str)
                            y = int(y_str)
                            if is_valid_date(y, m, d):
                                year, month, day = y, m, d
                except (ValueError, IndexError):
                    pass

            if year is not None:
                print(f"{year:04d}-{month:02d}-{day:02d}")
                break  # Exit
            else:
                pass

        except EOFError:
            # User pressed Ctrl+D (or Ctrl+Z on Windows)
            break
        except Exception:

            continue


if __name__ == '__main__':
    main()
