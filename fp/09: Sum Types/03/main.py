from enum import Enum


class CSVExportStatus(Enum):
    PENDING = 1
    PROCESSING = 2
    SUCCESS = 3
    FAILURE = 4


def get_csv_status(status, data):
    match status:
        case CSVExportStatus.PENDING:
            return ("Pending...", list(map(lambda row: list(map(str, row)), data)))
        case CSVExportStatus.PROCESSING:
            csv_rows = [",".join(row) for row in data]
            csv_data = "\n".join(csv_rows)
            return ("Processing...", csv_data)
        case CSVExportStatus.SUCCESS:
            return ("Success!", data)
        case CSVExportStatus.FAILURE:
            csv_rows = [",".join(list(map(str, row))) for row in data]
            csv_data = "\n".join(csv_rows)
            return ("Unknown error, retrying...", csv_data)
        case _:
            raise Exception("Unknown export status")
