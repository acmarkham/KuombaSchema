# Auto generated from kuombaschema.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-05-18T13:48:10
# Schema: KuombaSchema
#
# id: https://w3id.org/acmarkham/KuombaSchema
# description: Schema for multimodal ecological data
# license: MIT

import re
from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.metamodelcore import empty_dict
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import YAMLRoot
from rdflib import URIRef

from linkml_runtime.utils.metamodelcore import URIorCURIE, XSDDate

metamodel_version = "1.11.0"
version = None

# Namespaces
PATO = CurieNamespace("PATO", "http://purl.obolibrary.org/obo/PATO_")
BIOLINK = CurieNamespace("biolink", "https://w3id.org/biolink/")
EXAMPLE = CurieNamespace("example", "https://example.org/")
KUOMBASCHEMA = CurieNamespace(
    "kuombaschema", "https://w3id.org/acmarkham/KuombaSchema/"
)
LINKML = CurieNamespace("linkml", "https://w3id.org/linkml/")
SCHEMA = CurieNamespace("schema", "http://schema.org/")
DEFAULT_ = KUOMBASCHEMA


# Types


# Class references
class NamedThingId(URIorCURIE):
    pass


class PersonId(NamedThingId):
    pass


@dataclass(repr=False)
class NamedThing(YAMLRoot):
    """
    A generic grouping for any identifiable entity
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Thing"]
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = KUOMBASCHEMA.NamedThing

    id: Union[str, NamedThingId] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Person(NamedThing):
    """
    Represents a Person
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = KUOMBASCHEMA["Person"]
    class_class_curie: ClassVar[str] = "kuombaschema:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = KUOMBASCHEMA.Person

    id: Union[str, PersonId] = None
    primary_email: Optional[str] = None
    birth_date: Optional[Union[str, XSDDate]] = None
    age_in_years: Optional[int] = None
    vital_status: Optional[Union[str, "PersonStatus"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonId):
            self.id = PersonId(self.id)

        if self.primary_email is not None and not isinstance(self.primary_email, str):
            self.primary_email = str(self.primary_email)

        if self.birth_date is not None and not isinstance(self.birth_date, XSDDate):
            self.birth_date = XSDDate(self.birth_date)

        if self.age_in_years is not None and not isinstance(self.age_in_years, int):
            self.age_in_years = int(self.age_in_years)

        if self.vital_status is not None and not isinstance(
            self.vital_status, PersonStatus
        ):
            self.vital_status = PersonStatus(self.vital_status)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PersonCollection(YAMLRoot):
    """
    A holder for Person objects
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = KUOMBASCHEMA["PersonCollection"]
    class_class_curie: ClassVar[str] = "kuombaschema:PersonCollection"
    class_name: ClassVar[str] = "PersonCollection"
    class_model_uri: ClassVar[URIRef] = KUOMBASCHEMA.PersonCollection

    people: Optional[
        Union[
            dict[Union[str, PersonId], Union[dict, Person]], list[Union[dict, Person]]
        ]
    ] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(
            slot_name="people", slot_type=Person, key_name="id", keyed=True
        )

        super().__post_init__(**kwargs)


# Enumerations
class PersonStatus(EnumDefinitionImpl):
    ALIVE = PermissibleValue(
        text="ALIVE", description="the person is living", meaning=PATO["0001421"]
    )
    DEAD = PermissibleValue(
        text="DEAD", description="the person is deceased", meaning=PATO["0001422"]
    )
    UNKNOWN = PermissibleValue(
        text="UNKNOWN", description="the vital status is not known"
    )

    _defn = EnumDefinition(
        name="PersonStatus",
    )


# Slots
class slots:
    pass


slots.id = Slot(
    uri=SCHEMA.identifier,
    name="id",
    curie=SCHEMA.curie("identifier"),
    model_uri=KUOMBASCHEMA.id,
    domain=None,
    range=URIRef,
)

slots.name = Slot(
    uri=SCHEMA.name,
    name="name",
    curie=SCHEMA.curie("name"),
    model_uri=KUOMBASCHEMA.name,
    domain=None,
    range=Optional[str],
)

slots.description = Slot(
    uri=SCHEMA.description,
    name="description",
    curie=SCHEMA.curie("description"),
    model_uri=KUOMBASCHEMA.description,
    domain=None,
    range=Optional[str],
)

slots.primary_email = Slot(
    uri=SCHEMA.email,
    name="primary_email",
    curie=SCHEMA.curie("email"),
    model_uri=KUOMBASCHEMA.primary_email,
    domain=None,
    range=Optional[str],
)

slots.birth_date = Slot(
    uri=SCHEMA.birthDate,
    name="birth_date",
    curie=SCHEMA.curie("birthDate"),
    model_uri=KUOMBASCHEMA.birth_date,
    domain=None,
    range=Optional[Union[str, XSDDate]],
)

slots.age_in_years = Slot(
    uri=KUOMBASCHEMA.age_in_years,
    name="age_in_years",
    curie=KUOMBASCHEMA.curie("age_in_years"),
    model_uri=KUOMBASCHEMA.age_in_years,
    domain=None,
    range=Optional[int],
)

slots.vital_status = Slot(
    uri=KUOMBASCHEMA.vital_status,
    name="vital_status",
    curie=KUOMBASCHEMA.curie("vital_status"),
    model_uri=KUOMBASCHEMA.vital_status,
    domain=None,
    range=Optional[Union[str, "PersonStatus"]],
)

slots.personCollection__people = Slot(
    uri=KUOMBASCHEMA.people,
    name="personCollection__people",
    curie=KUOMBASCHEMA.curie("people"),
    model_uri=KUOMBASCHEMA.personCollection__people,
    domain=None,
    range=Optional[
        Union[
            dict[Union[str, PersonId], Union[dict, Person]], list[Union[dict, Person]]
        ]
    ],
)

slots.Person_primary_email = Slot(
    uri=SCHEMA.email,
    name="Person_primary_email",
    curie=SCHEMA.curie("email"),
    model_uri=KUOMBASCHEMA.Person_primary_email,
    domain=Person,
    range=Optional[str],
    pattern=re.compile(r"^\S+@[\S+\.]+\S+"),
)
