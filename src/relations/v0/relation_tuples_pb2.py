# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: relations/v0/relation_tuples.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from relations.v0 import common_pb2 as relations_dot_v0_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"relations/v0/relation_tuples.proto\x12\x13kessel.relations.v0\x1a\x1cgoogle/api/annotations.proto\x1a\x19relations/v0/common.proto\"X\n\x13\x43reateTuplesRequest\x12\x0e\n\x06upsert\x18\x01 \x01(\x08\x12\x31\n\x06tuples\x18\x02 \x03(\x0b\x32!.kessel.relations.v0.Relationship\"\x16\n\x14\x43reateTuplesResponse\"\x9d\x01\n\x11ReadTuplesRequest\x12\x38\n\x06\x66ilter\x18\x01 \x01(\x0b\x32(.kessel.relations.v0.RelationTupleFilter\x12?\n\npagination\x18\x02 \x01(\x0b\x32&.kessel.relations.v0.RequestPaginationH\x00\x88\x01\x01\x42\r\n\x0b_pagination\"\x83\x01\n\x12ReadTuplesResponse\x12\x30\n\x05tuple\x18\x01 \x01(\x0b\x32!.kessel.relations.v0.Relationship\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.kessel.relations.v0.ResponsePagination\"O\n\x13\x44\x65leteTuplesRequest\x12\x38\n\x06\x66ilter\x18\x01 \x01(\x0b\x32(.kessel.relations.v0.RelationTupleFilter\"\x16\n\x14\x44\x65leteTuplesResponse\"\x9d\x02\n\x13RelationTupleFilter\x12\x1f\n\x12resource_namespace\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x1a\n\rresource_type\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x18\n\x0bresource_id\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x15\n\x08relation\x18\x04 \x01(\tH\x03\x88\x01\x01\x12?\n\x0esubject_filter\x18\x05 \x01(\x0b\x32\".kessel.relations.v0.SubjectFilterH\x04\x88\x01\x01\x42\x15\n\x13_resource_namespaceB\x10\n\x0e_resource_typeB\x0e\n\x0c_resource_idB\x0b\n\t_relationB\x11\n\x0f_subject_filter\"\xbd\x01\n\rSubjectFilter\x12\x1e\n\x11subject_namespace\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x19\n\x0csubject_type\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x17\n\nsubject_id\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x15\n\x08relation\x18\x04 \x01(\tH\x03\x88\x01\x01\x42\x14\n\x12_subject_namespaceB\x0f\n\r_subject_typeB\r\n\x0b_subject_idB\x0b\n\t_relation2\xfe\x02\n\x12KesselTupleService\x12z\n\x0c\x43reateTuples\x12(.kessel.relations.v0.CreateTuplesRequest\x1a).kessel.relations.v0.CreateTuplesResponse\"\x15\x82\xd3\xe4\x93\x02\x0f\"\n/v0/tuples:\x01*\x12s\n\nReadTuples\x12&.kessel.relations.v0.ReadTuplesRequest\x1a\'.kessel.relations.v0.ReadTuplesResponse\"\x12\x82\xd3\xe4\x93\x02\x0c\x12\n/v0/tuples0\x01\x12w\n\x0c\x44\x65leteTuples\x12(.kessel.relations.v0.DeleteTuplesRequest\x1a).kessel.relations.v0.DeleteTuplesResponse\"\x12\x82\xd3\xe4\x93\x02\x0c*\n/v0/tuplesBG\n#org.project_kessel.api.relations.v0P\x01Z\x1e\x63iam-rebac/api/relations/v0;v0b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'relations.v0.relation_tuples_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n#org.project_kessel.api.relations.v0P\001Z\036ciam-rebac/api/relations/v0;v0'
  _globals['_KESSELTUPLESERVICE'].methods_by_name['CreateTuples']._loaded_options = None
  _globals['_KESSELTUPLESERVICE'].methods_by_name['CreateTuples']._serialized_options = b'\202\323\344\223\002\017\"\n/v0/tuples:\001*'
  _globals['_KESSELTUPLESERVICE'].methods_by_name['ReadTuples']._loaded_options = None
  _globals['_KESSELTUPLESERVICE'].methods_by_name['ReadTuples']._serialized_options = b'\202\323\344\223\002\014\022\n/v0/tuples'
  _globals['_KESSELTUPLESERVICE'].methods_by_name['DeleteTuples']._loaded_options = None
  _globals['_KESSELTUPLESERVICE'].methods_by_name['DeleteTuples']._serialized_options = b'\202\323\344\223\002\014*\n/v0/tuples'
  _globals['_CREATETUPLESREQUEST']._serialized_start=116
  _globals['_CREATETUPLESREQUEST']._serialized_end=204
  _globals['_CREATETUPLESRESPONSE']._serialized_start=206
  _globals['_CREATETUPLESRESPONSE']._serialized_end=228
  _globals['_READTUPLESREQUEST']._serialized_start=231
  _globals['_READTUPLESREQUEST']._serialized_end=388
  _globals['_READTUPLESRESPONSE']._serialized_start=391
  _globals['_READTUPLESRESPONSE']._serialized_end=522
  _globals['_DELETETUPLESREQUEST']._serialized_start=524
  _globals['_DELETETUPLESREQUEST']._serialized_end=603
  _globals['_DELETETUPLESRESPONSE']._serialized_start=605
  _globals['_DELETETUPLESRESPONSE']._serialized_end=627
  _globals['_RELATIONTUPLEFILTER']._serialized_start=630
  _globals['_RELATIONTUPLEFILTER']._serialized_end=915
  _globals['_SUBJECTFILTER']._serialized_start=918
  _globals['_SUBJECTFILTER']._serialized_end=1107
  _globals['_KESSELTUPLESERVICE']._serialized_start=1110
  _globals['_KESSELTUPLESERVICE']._serialized_end=1492
# @@protoc_insertion_point(module_scope)
