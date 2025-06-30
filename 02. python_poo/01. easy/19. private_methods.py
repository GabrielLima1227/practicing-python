class Internal:
    def __init__(self, secret_data: str):
        self._secret_data = secret_data

    def _process_data(self) -> str:
        processed_data = f"PROCESSED: {self._secret_data.upper()}"
        print("Internal: Secret data processed internally.")
        return processed_data

    def display_data(self) -> None:
        data_to_display = self._process_data()
        print(f"Internal: Displaying processed data: '{data_to_display}'")

my_internal_object = Internal("very confidential information")

print("\nCalling the public 'display_data' method:")
my_internal_object.display_data()

print(f"\nAccessing _secret_data directly (discouraged): {my_internal_object._secret_data}")

print("\nCalling _process_data directly (discouraged):")
manual_data = my_internal_object._process_data()
print(f"Result of direct call to _process_data: '{manual_data}'")

my_internal_object._secret_data = "NEW SECRET INFORMATION"
print(f"\n_secret_data modified directly to: {my_internal_object._secret_data}")
my_internal_object.display_data()