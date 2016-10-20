import uncertainpy

model_path = "../../uncertainpy/models/neuron_models/dLGN_modelDB/"


parameterlist = [["cap", 1.1, None],
                 ["Rm", 22000, None],
                 ["Vrest", -63, None],
                 ["Epas", -67, None],
                 ["gna", 0.09, None],
                 ["nash", -52.6, None],
                 ["gkdr", 0.37, None],
                 ["kdrsh", -51.2, None],
                 ["gahp", 6.4e-5, None],
                 ["gcat", 1.17e-5, None]]


parameters = uncertainpy.Parameters(parameterlist)
model = uncertainpy.NeuronModel(parameters=parameters,
                                model_path=model_path,
                                adaptive_model=True)

model.setAllDistributions(uncertainpy.Distribution(0.05).uniform)

features = uncertainpy.NeuronFeatures(features_to_run="all")

exploration = uncertainpy.UncertaintyEstimations(model,
                                                 features=features,
                                                 CPUs=7,
                                                 save_figures=True)


percentages = [0.01, 0.05, 0.1]

distributions = {"uniform": percentages}
exploration.exploreParameters(distributions)
