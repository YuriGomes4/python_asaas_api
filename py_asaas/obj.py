import json


def cliente(name=None, email=None, phone=None, mobile_phone=None, cpf_cnpj=None, postal_code=None, address=None, address_number=None, complement=None, province=None, external_reference=None, notification_disabled=None, additional_emails=None, municipal_inscription=None, state_inscription=None, observations=None):
        customer_data = {
            "name": name,
            "email": email,
            "phone": phone,
            "mobilePhone": mobile_phone,
            "cpfCnpj": cpf_cnpj,
            "postalCode": postal_code,
            "address": address,
            "addressNumber": address_number,
            "complement": complement,
            "province": province,
            "externalReference": external_reference,
            "notificationDisabled": notification_disabled,
            "additionalEmails": additional_emails,
            "municipalInscription": municipal_inscription,
            "stateInscription": state_inscription,
            "observations": observations
        }
        return customer_data

def assinatura(customer_id=None, billing_type=None, next_due_date=None, value=None, cycle=None, description=None, discount_value=None, discount_due_date_limit_days=None, fine_value=None, interest_value=None, end_date=None):
    billing_data = {
        "customer": customer_id,
        "billingType": billing_type,
        "nextDueDate": next_due_date,
        "value": value,
        "cycle": cycle,
        "description": description,
        "endDate": end_date,
    }

    if discount_value or discount_due_date_limit_days:
        billing_data["discount"] = {"value": discount_value, "dueDateLimitDays": discount_due_date_limit_days}

    if fine_value:
        billing_data["fine"] = {"value": fine_value}

    if interest_value:
        billing_data["interest"] = {"value": interest_value}

    for key in list(billing_data.keys()):
        if billing_data[key] == None:
            del billing_data[key]

    return billing_data

class billingType:

    nao_definido = "UNDEFINED"
    pix = "PIX"
    cartao_credito = "CREDIT_CARD"
    boleto = "BOLETO"

class cycle:

    semanal = "WEEKLY"
    quinzenal = "BIWEEKLY"
    mensal = "MONTHLY"
    bimensal = "BIMONTHLY"
    trimestral = "QUARTERLY"
    semi_anual = "SEMIANNUALLY"
    anual = "MONTHLY"