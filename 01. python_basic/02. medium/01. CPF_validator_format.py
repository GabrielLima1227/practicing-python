# This code only verifies the CPF format, not whether it is valid.
def cpf_format(cpf_number: str) -> str:
    if cpf_number.count('.') == 2 and cpf_number.count('-') == 1 and len(cpf_number) == 14:
        return "Valid CPF"
    else:
        return "Invalid CPF"

cpf = input("Insert your CPF: ").strip()
print(cpf_format(cpf))