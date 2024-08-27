from os import PathLike
from anyio import run, open_file
from anyio.streams.file import FileReadStream, FileWriteStream
from httpx import AsyncClient, HTTPError


async def download_openapi_spec(url: str, output_file: str | PathLike[str]) -> None:
    """Function which downloads OpenAPI spec from given URL and saves it to an output file.

    args:
        url (str): URL of OpenAPI spec in JSON format.
        output_file (str | PathLike[str]): Path to the output file where OpenAPI spec will be saved.

    returns:
        None
    """
    async with AsyncClient() as client:
        try:
            # Fetch the OpenAPI spec file from proivded URL
            response = await client.get(url)

            # Raise an exception if the response status code is not 200, ensuring we only proceed
            response.raise_for_status()

            try:
                # Open the file asynchronously in write mode
                async with await open_file(output_file, "wb") as file:
                    # Write the response content to the output file
                    await file.write(response.content)

            except Exception as exc:
                print(f"An error occurred saving OpenAPI spec file: {exc}")

        except HTTPError as exc:
            print(f"An error occurred fetching OpenAPI spec file: {exc} from {url}")
            return


async def main():
    # Set the URL of OpenAPI spec and output file path
    url = "http://localhost:8000/openapi.jso        n"
    output_path = "../../openapi.json"

    print(f"Downloading OpenAPI spec from {url} and saving it to {output_path}...")
    print("Please wait...")

    # Download OpenAPI spec from URL and save it to output file
    await download_openapi_spec(url, output_path)
    print(f"OpenAPI spec downloaded and saved to {output_path}")


# Run the main function
if __name__ == "__main__":
    run(main)
