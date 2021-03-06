# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Qot_GetOptionChain.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import Common_pb2 as Common__pb2
import Qot_Common_pb2 as Qot__Common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Qot_GetOptionChain.proto',
  package='Qot_GetOptionChain',
  syntax='proto2',
  serialized_pb=_b('\n\x18Qot_GetOptionChain.proto\x12\x12Qot_GetOptionChain\x1a\x0c\x43ommon.proto\x1a\x10Qot_Common.proto\"\x88\x01\n\x03\x43\x32S\x12#\n\x05owner\x18\x01 \x02(\x0b\x32\x14.Qot_Common.Security\x12\x17\n\x0findexOptionType\x18\x06 \x01(\x05\x12\x0c\n\x04type\x18\x02 \x01(\x05\x12\x11\n\tcondition\x18\x03 \x01(\x05\x12\x11\n\tbeginTime\x18\x04 \x02(\t\x12\x0f\n\x07\x65ndTime\x18\x05 \x02(\t\"g\n\nOptionItem\x12,\n\x04\x63\x61ll\x18\x01 \x01(\x0b\x32\x1e.Qot_Common.SecurityStaticInfo\x12+\n\x03put\x18\x02 \x01(\x0b\x32\x1e.Qot_Common.SecurityStaticInfo\"j\n\x0bOptionChain\x12\x12\n\nstrikeTime\x18\x01 \x02(\t\x12.\n\x06option\x18\x02 \x03(\x0b\x32\x1e.Qot_GetOptionChain.OptionItem\x12\x17\n\x0fstrikeTimestamp\x18\x03 \x01(\x01\";\n\x03S2C\x12\x34\n\x0boptionChain\x18\x01 \x03(\x0b\x32\x1f.Qot_GetOptionChain.OptionChain\"/\n\x07Request\x12$\n\x03\x63\x32s\x18\x01 \x02(\x0b\x32\x17.Qot_GetOptionChain.C2S\"h\n\x08Response\x12\x15\n\x07retType\x18\x01 \x02(\x05:\x04-400\x12\x0e\n\x06retMsg\x18\x02 \x01(\t\x12\x0f\n\x07\x65rrCode\x18\x03 \x01(\x05\x12$\n\x03s2c\x18\x04 \x01(\x0b\x32\x17.Qot_GetOptionChain.S2C*b\n\x0eOptionCondType\x12\x19\n\x15OptionCondType_Unknow\x10\x00\x12\x19\n\x15OptionCondType_WithIn\x10\x01\x12\x1a\n\x16OptionCondType_Outside\x10\x02\x42\x15\n\x13\x63om.futu.openapi.pb')
  ,
  dependencies=[Common__pb2.DESCRIPTOR,Qot__Common__pb2.DESCRIPTOR,])

_OPTIONCONDTYPE = _descriptor.EnumDescriptor(
  name='OptionCondType',
  full_name='Qot_GetOptionChain.OptionCondType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OptionCondType_Unknow', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OptionCondType_WithIn', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OptionCondType_Outside', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=648,
  serialized_end=746,
)
_sym_db.RegisterEnumDescriptor(_OPTIONCONDTYPE)

OptionCondType = enum_type_wrapper.EnumTypeWrapper(_OPTIONCONDTYPE)
OptionCondType_Unknow = 0
OptionCondType_WithIn = 1
OptionCondType_Outside = 2



_C2S = _descriptor.Descriptor(
  name='C2S',
  full_name='Qot_GetOptionChain.C2S',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='owner', full_name='Qot_GetOptionChain.C2S.owner', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='indexOptionType', full_name='Qot_GetOptionChain.C2S.indexOptionType', index=1,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='Qot_GetOptionChain.C2S.type', index=2,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='condition', full_name='Qot_GetOptionChain.C2S.condition', index=3,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='beginTime', full_name='Qot_GetOptionChain.C2S.beginTime', index=4,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endTime', full_name='Qot_GetOptionChain.C2S.endTime', index=5,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=81,
  serialized_end=217,
)


_OPTIONITEM = _descriptor.Descriptor(
  name='OptionItem',
  full_name='Qot_GetOptionChain.OptionItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='call', full_name='Qot_GetOptionChain.OptionItem.call', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='put', full_name='Qot_GetOptionChain.OptionItem.put', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=219,
  serialized_end=322,
)


_OPTIONCHAIN = _descriptor.Descriptor(
  name='OptionChain',
  full_name='Qot_GetOptionChain.OptionChain',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='strikeTime', full_name='Qot_GetOptionChain.OptionChain.strikeTime', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='option', full_name='Qot_GetOptionChain.OptionChain.option', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='strikeTimestamp', full_name='Qot_GetOptionChain.OptionChain.strikeTimestamp', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=324,
  serialized_end=430,
)


_S2C = _descriptor.Descriptor(
  name='S2C',
  full_name='Qot_GetOptionChain.S2C',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='optionChain', full_name='Qot_GetOptionChain.S2C.optionChain', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=432,
  serialized_end=491,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='Qot_GetOptionChain.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='c2s', full_name='Qot_GetOptionChain.Request.c2s', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=493,
  serialized_end=540,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='Qot_GetOptionChain.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='retType', full_name='Qot_GetOptionChain.Response.retType', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=True, default_value=-400,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='retMsg', full_name='Qot_GetOptionChain.Response.retMsg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='errCode', full_name='Qot_GetOptionChain.Response.errCode', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='s2c', full_name='Qot_GetOptionChain.Response.s2c', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=542,
  serialized_end=646,
)

_C2S.fields_by_name['owner'].message_type = Qot__Common__pb2._SECURITY
_OPTIONITEM.fields_by_name['call'].message_type = Qot__Common__pb2._SECURITYSTATICINFO
_OPTIONITEM.fields_by_name['put'].message_type = Qot__Common__pb2._SECURITYSTATICINFO
_OPTIONCHAIN.fields_by_name['option'].message_type = _OPTIONITEM
_S2C.fields_by_name['optionChain'].message_type = _OPTIONCHAIN
_REQUEST.fields_by_name['c2s'].message_type = _C2S
_RESPONSE.fields_by_name['s2c'].message_type = _S2C
DESCRIPTOR.message_types_by_name['C2S'] = _C2S
DESCRIPTOR.message_types_by_name['OptionItem'] = _OPTIONITEM
DESCRIPTOR.message_types_by_name['OptionChain'] = _OPTIONCHAIN
DESCRIPTOR.message_types_by_name['S2C'] = _S2C
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.enum_types_by_name['OptionCondType'] = _OPTIONCONDTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

C2S = _reflection.GeneratedProtocolMessageType('C2S', (_message.Message,), dict(
  DESCRIPTOR = _C2S,
  __module__ = 'Qot_GetOptionChain_pb2'
  # @@protoc_insertion_point(class_scope:Qot_GetOptionChain.C2S)
  ))
_sym_db.RegisterMessage(C2S)

OptionItem = _reflection.GeneratedProtocolMessageType('OptionItem', (_message.Message,), dict(
  DESCRIPTOR = _OPTIONITEM,
  __module__ = 'Qot_GetOptionChain_pb2'
  # @@protoc_insertion_point(class_scope:Qot_GetOptionChain.OptionItem)
  ))
_sym_db.RegisterMessage(OptionItem)

OptionChain = _reflection.GeneratedProtocolMessageType('OptionChain', (_message.Message,), dict(
  DESCRIPTOR = _OPTIONCHAIN,
  __module__ = 'Qot_GetOptionChain_pb2'
  # @@protoc_insertion_point(class_scope:Qot_GetOptionChain.OptionChain)
  ))
_sym_db.RegisterMessage(OptionChain)

S2C = _reflection.GeneratedProtocolMessageType('S2C', (_message.Message,), dict(
  DESCRIPTOR = _S2C,
  __module__ = 'Qot_GetOptionChain_pb2'
  # @@protoc_insertion_point(class_scope:Qot_GetOptionChain.S2C)
  ))
_sym_db.RegisterMessage(S2C)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'Qot_GetOptionChain_pb2'
  # @@protoc_insertion_point(class_scope:Qot_GetOptionChain.Request)
  ))
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'Qot_GetOptionChain_pb2'
  # @@protoc_insertion_point(class_scope:Qot_GetOptionChain.Response)
  ))
_sym_db.RegisterMessage(Response)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\023com.futu.openapi.pb'))
# @@protoc_insertion_point(module_scope)
