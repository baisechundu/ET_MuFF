# -*- coding:utf-8 -*-
import os
from corpora_generation_origin import pretrain_dataset_generation
from extract_feature_packet import PacketFlowExtract

if __name__ == '__main__':
    # corpora-generate
    # file_path = r""
    # pretrain_dataset_generation(file_path)

    # data_with_label-generate
    cur_path = os.path.dirname(os.path.realpath(__file__))
    print(cur_path)
    parent_path = os.path.dirname(cur_path)
    dataset_type = "malware_pcap"
    dataset_split_type = ""
    feature_version = "v2"
    session_start_position = 0

    pcap_path = os.path.join(parent_path, "data/%s/%s" % (dataset_type, dataset_split_type))

    dataset_save_path = os.path.join(parent_path, "data/data_with_label/%s/%s/flow/result_%s_%s" % (
        dataset_type, dataset_split_type, feature_version, str(session_start_position + 1)))

    packet_extract = PacketFlowExtract(pcap_root_path=pcap_path,
                                       samples_list=[100],
                                       dataset_save_path=dataset_save_path,
                                       session_start_position=session_start_position,
                                       version=feature_version).generation()
