#!/usr/bin/env python
import sys
import fields

file = sys.argv[1]

# print("Processing file: {}".format(file))

# sep = ","
sep = "\t"


class Field(object):
    def __init__(self, name, field_props, source_string):
        self.source_string = source_string
        self.field_props = field_props
        start = field_props.get("start") - 1
        end = field_props.get("end")
        self.value = source_string[start:end]

    def __str__(self):
        return str(self.value)


class Row(object):
    def __init__(self, source_string, ed_fields, candidate_fields):
        self.source_string = source_string
        self.ed_fields_list = ed_fields
        self.candidate_fields_list = candidate_fields

        formatted_district_field = (
            Field("", self.ed_fields_list["Formatted District"], self.source_string)
        )
        self.is_total = formatted_district_field.value.strip() == "TOTAL"

        id_field = Field("ID",
                         self.ed_fields_list["ID"],
                         self.source_string)
        self.id = id_field.value

        num_candidates_field_props = self.ed_fields_list[
            "Number of Candidates"
        ]
        num_candiates_field = Field("Number of Candidates",
                                    num_candidates_field_props,
                                    self.source_string)
        self.num_candidates = int(num_candiates_field.value)

    def get_election_fields_as_csv(self):
        if self.is_total:
            return ""

        fields = [Field(k, v, self.source_string) for (k, v)
                  in self.ed_fields_list.items()]

        str = ""
        for f in fields:
            next = f.__str__().strip()
            str += "{}{}".format(sep, next)

        return str[1:]

    def get_election_totals_fields_only_as_csv(self):
        if not self.is_total:
            return ""

        fields = [Field(k, v, self.source_string) for (k, v)
                  in self.ed_fields_list.items()]

        str = ""
        for f in fields:
            next = f.__str__().strip()
            str += "{}{}".format(sep, next)

        return str[1:]


    def get_candidate_fields_as_csv(self):
        if self.is_total:
            return ""

        fields = []
        for num in range(self.num_candidates):
            fields.append(self.id)
            for k in self.candidate_fields_list:
                fields.append(
                    Field(k, self.candidate_fields_list[k](num),
                          self.source_string).value.strip())

        i = 0
        str = ""
        for f in fields:
            i += 1
            str += f
            if i % 4 == 0:
                str += "\n"
            else:
                str += "\t"

        return str


def get_ed_headers_list():
    headers = []
    for k in fields.ed_fields:
        headers.append(k)
    return sep.join(headers)


def get_candidate_headers_list():
    headers = ["ID", "Candidate Party Name", "Candidate Name", "Candidate Tally"]
    return sep.join(headers)


with open(file) as infile:
    # For generating candidates
    #
    # print(get_candidate_headers_list(), end="\n", flush=True)
    # for line in infile:
    #     row = Row(line, fields.ed_fields, fields.candidate_fields)
    #     print(row.get_candidate_fields_as_csv(), end="")

    # For generating elections
    #
    # print(get_ed_headers_list(), end="\n")
    # for line in infile:
    #     row = Row(line, fields.ed_fields, fields.candidate_fields)
    #     print(row.get_election_fields_as_csv(), end="\n")

    # For generating election totals *ONLY*
    #
    print(get_ed_headers_list(), end="\n")
    for line in infile:
        row = Row(line, fields.ed_fields, fields.candidate_fields)
        row_str = row.get_election_totals_fields_only_as_csv() 
        if row_str != "":
            print(row_str, end="\n")
