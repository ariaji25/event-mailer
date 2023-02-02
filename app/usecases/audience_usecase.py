from typing import List

from app.repositories import audiences_respository, event_repository
from app.models.audience_model import AudienceModel, GetAudienceParam


def audience_to_audience_model(audience: audiences_respository.Audience) -> AudienceModel:
    return AudienceModel(
        id=audience.id,
        name=audience.name,
        email=audience.email,
        event_id=audience.event_id.id,
    )


def create_audience_usecase(audience: AudienceModel) -> tuple[int, str]:
    event_exist = event_repository.is_exist(audience.event_id)
    if not event_exist:
        return 0, 'event-{}-notfound'.format(audience.event_id)
    is_exist = audiences_respository.is_exist(audience.email, event_id=audience.event_id)
    if is_exist:
        return 0, 'audience-{}-is-exist'.format(audience.email)
    audience_id, err = audiences_respository.create_audience(
        event_id=audience.event_id,
        name=audience.name,
        email=audience.email
    )
    return audience_id, err


def get_audience_usecase(param: GetAudienceParam) -> tuple[List[AudienceModel], str]:
    event_exist = event_repository.is_exist(param.event_id)
    if not event_exist:
        return [], 'event-{}-notfound'.format(param.event_id)
    audiences, err = audiences_respository.get_audience_by_event_id(
        param.event_id, param.page)
    audiences = [audience_to_audience_model(a) for a in audiences]
    return audiences, err
