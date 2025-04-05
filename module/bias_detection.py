from aif360.datasets import BinaryLabelDataset
from aif360.metrics import BinaryLabelDatasetMetric


def load_dataset(df, label_name, protected_attribute_name):
	"""Load dataset into BinaryLabelDataset format."""
	return BinaryLabelDataset(df=df, label_names=[label_name], protected_attribute_names=[protected_attribute_name])


def calculate_fairness_metrics(dataset, privileged_groups, unprivileged_groups):
	"""Calculate fairness metrics for the dataset."""
	metric = BinaryLabelDatasetMetric(dataset, privileged_groups=privileged_groups,
									  unprivileged_groups=unprivileged_groups)
	disparate_impact = metric.disparate_impact()
	return disparate_impact


def mitigate_bias(dataset, privileged_groups, unprivileged_groups):
	"""Apply reweighing to mitigate bias in the dataset."""
	reweighing = Reweighing(unprivileged_groups=unprivileged_groups, privileged_groups=privileged_groups)
	dataset_transf = reweighing.fit_transform(dataset)
	return dataset_transf


def evaluate_bias(df, label_name, protected_attribute_name, privileged_groups, unprivileged_groups):
	"""Evaluate and mitigate bias in the dataset."""
	dataset = load_dataset(df, label_name, protected_attribute_name)
	initial_disparate_impact = calculate_fairness_metrics(dataset, privileged_groups, unprivileged_groups)
	print(f"Initial Disparate Impact: {initial_disparate_impact}")

	dataset_transf = mitigate_bias(dataset, privileged_groups, unprivileged_groups)
	mitigated_disparate_impact = calculate_fairness_metrics(dataset_transf, privileged_groups, unprivileged_groups)
	print(f"Disparate Impact after Mitigation: {mitigated_disparate_impact}")

	return dataset_transf
