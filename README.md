# Task 1 – Netflix Movies & TV Shows Dataset Cleaning

## Objective:
Clean a raw Netflix dataset by handling missing values, duplicates, and inconsistent formatting.

## Tools Used:
- Python 3.x
- Pandas

## Cleaning Steps Performed:

1. **Removed duplicate rows** using `drop_duplicates()`.
2. **Handled missing values**:
   - `director` → replaced with `'Unspecified'`
   - `cast` → replaced with `'Unknown'`
   - `country` → filled using mode (most common country)
   - `rating` → replaced with `'Not Rated'`
3. **Cleaned `date_added`**:
   - Converted to datetime with `pd.to_datetime()`
   - Filled any invalid/missing dates with `'2020-01-01'`
4. **Standardized column names** (lowercase + underscores).
5. **Simplified `cast`** → kept only the first actor/actress.
6. **Cleaned `show_id`** → removed the 's' prefix.
7. **Extracted `year_added` and `month_added`** from `date_added`.
8. **Saved the cleaned dataset** as `netflix_titles.csv`.

## Files in This Repo:
- `netflix_cleaning_task.py` – Python code for cleaning
- `netflix_titles.csv` – Cleaned dataset
- `README.md` – Task summary and steps

## Output:
Cleaned dataset is ready for analysis or machine learning tasks.

---