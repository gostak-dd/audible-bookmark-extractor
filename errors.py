class ExternalError:

    def __init__(self, initiator, asin, error):
        self.initiator = initiator
        self.asin = asin
        self.error = error

    def show_error(self):
        print(
            f"Error while executing {self.initiator}, for ASIN: {self.asin}, msg: {self.error}")


class DownloadUnavailableError(Exception):
    """Raised when Audible's download endpoint doesn't redirect to a file.

    Usually means the title isn't available for direct AAX download (e.g. it's
    AAXC-only, or the asin/session is otherwise rejected) rather than a network issue.
    """

    def __init__(self, status_code, body):
        self.status_code = status_code
        self.body = body
        snippet = (body or "").strip()[:200]
        super().__init__(
            f"Audible did not provide a download link (HTTP {status_code}). "
            f"This title may not support direct AAX download. Response: {snippet}"
        )
