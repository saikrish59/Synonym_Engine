from cache_utils import get_from_cache, save_to_cache
from db_utils import fetch_all_synonyms

def main():
    word_key = "synonyms:all"
    cached_data = get_from_cache(word_key)

    if cached_data:
        print("Fetched from cache:")
        print(cached_data)
    else:
        print("Cache miss. Fetching from DB...")
        data = fetch_all_synonyms()
        save_to_cache(word_key, data, ttl=3600)
        print(data)

if __name__ == "__main__":
    main()
