from ProgSnap2Lib.progsnap import ProgSnap2Dataset, PS2

for dataset_folder in ['cwo-f19', 'isnap-f17']:

    print('loading dataset: ' + dataset_folder)
    dataset = ProgSnap2Dataset('data/' + dataset_folder)
    main_table = dataset.get_main_table()
    print(main_table.head())

    print(main_table[PS2.SubjectID].unique())