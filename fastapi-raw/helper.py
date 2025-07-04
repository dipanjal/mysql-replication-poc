from collections.abc import Sequence


class Parser:
    @staticmethod
    def to_dicts(rows: Sequence[tuple], field_sequence: list[str]) -> list[dict[str, any]]:
        records: list = []
        for row in rows:
            record: dict[str, any] = {}
            for i in range(len(field_sequence)):
                field_name = field_sequence[i]
                field_value = row[i]
                record[field_name] = field_value
            records.append(record)
        return records

    @staticmethod
    def to_dict(row: tuple, field_sequence: list[str]) -> dict[str, any]:
        record: dict[str, any] = {}
        for i in range(len(field_sequence)):
            field_name = field_sequence[i]
            field_value = row[i]
            record[field_name] = field_value
        return record