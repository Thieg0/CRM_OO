from .report import Report

class AnalyticsManager:
    def __init__(self, contact_manager, sales_pipeline, lead_manager):
        self.contact_manager = contact_manager
        self.sales_pipeline = sales_pipeline
        self.lead_manager = lead_manager
        self.reports = []

    def generate_sales_report(self):
        """Gera relatório de vendas"""
        data = {
            'total_opportunities': len(self.sales_pipeline.opportunities),
            'by_stage': self._get_opportunities_by_stage(),
            'total_value': self._calculate_total_value(),
            'conversion_rate': self._calculate_conversion_rate()
        }
        report = Report("Sales Performance Report", "sales", data)
        self.reports.append(report)
        return report

    def generate_lead_report(self):
        """Gera relatório de leads"""
        data = {
            'total_leads': len(self.lead_manager.leads),
            'by_status': self._get_leads_by_status(),
            'by_source': self._get_leads_by_source(),
            'conversion_funnel': self._get_conversion_funnel()
        }
        report = Report("Lead Analysis Report", "leads", data)
        self.reports.append(report)
        return report

    def generate_pipeline_report(self):
        """Gera relatório do pipeline"""
        data = {
            'stage_distribution': self._get_opportunities_by_stage(),
            'value_by_stage': self._get_value_by_stage(),
            'average_deal_size': self._calculate_average_deal_size()
        }
        report = Report("Pipeline Analysis Report", "pipeline", data)
        self.reports.append(report)
        return report

    def list_reports(self):
        """Lista todos os relatórios gerados"""
        if not self.reports:
            print("No reports generated yet.")
            return

        for i, report in enumerate(self.reports, 1):
            print(f"\n{i}. {report}")

    def view_report(self, index):
        """Visualiza um relatório específico"""
        if 0 <= index < len(self.reports):
            report = self.reports[index]
            print(f"\n=== {report.title} ===")
            print(f"Generated at: {report.generated_at.strftime('%d/%m/%Y %H:%M')}")
            print("\nResults:")
            
            if report.report_type == "sales":
                self._display_sales_report(report.data)
            elif report.report_type == "leads":
                self._display_lead_report(report.data)
            elif report.report_type == "pipeline":
                self._display_pipeline_report(report.data)
        else:
            print("Invalid report index.")

    # Métodos auxiliares privados
    def _get_opportunities_by_stage(self):
        stages = {}
        for opp in self.sales_pipeline.opportunities.values():
            stages[opp.stage] = stages.get(opp.stage, 0) + 1
        return stages

    def _calculate_total_value(self):
        return sum(opp.value for opp in self.sales_pipeline.opportunities.values())

    def _calculate_conversion_rate(self):
        closed_won = sum(1 for opp in self.sales_pipeline.opportunities.values() if opp.stage == "Closed")
        total = len(self.sales_pipeline.opportunities)
        return (closed_won / total * 100) if total > 0 else 0

    def _get_leads_by_status(self):
        status_count = {}
        for lead in self.lead_manager.leads.values():
            status_count[lead.status] = status_count.get(lead.status, 0) + 1
        return status_count

    def _get_leads_by_source(self):
        source_count = {}
        for lead in self.lead_manager.leads.values():
            source_count[lead.source] = source_count.get(lead.source, 0) + 1
        return source_count

    def _get_conversion_funnel(self):
        return {
            'total_leads': len(self.lead_manager.leads),
            'qualified_leads': sum(1 for lead in self.lead_manager.leads.values() if lead.status == "Qualified"),
            'opportunities': len(self.sales_pipeline.opportunities),
            'closed_deals': sum(1 for opp in self.sales_pipeline.opportunities.values() if opp.stage == "Closed")
        }

    def _get_value_by_stage(self):
        value_by_stage = {}
        for opp in self.sales_pipeline.opportunities.values():
            value_by_stage[opp.stage] = value_by_stage.get(opp.stage, 0) + opp.value
        return value_by_stage

    def _calculate_average_deal_size(self):
        total_value = self._calculate_total_value()
        total_deals = len(self.sales_pipeline.opportunities)
        return total_value / total_deals if total_deals > 0 else 0

    # Métodos de exibição
    def _display_sales_report(self, data):
        print(f"\nTotal Opportunities: {data['total_opportunities']}")
        print(f"Total Value: R$ {data['total_value']:.2f}")
        print(f"Conversion Rate: {data['conversion_rate']:.1f}%")
        print("\nOpportunities by Stage:")
        for stage, count in data['by_stage'].items():
            print(f"- {stage}: {count}")

    def _display_lead_report(self, data):
        print(f"\nTotal Leads: {data['total_leads']}")
        print("\nLeads by Status:")
        for status, count in data['by_status'].items():
            print(f"- {status}: {count}")
        print("\nLeads by Source:")
        for source, count in data['by_source'].items():
            print(f"- {source}: {count}")
        print("\nConversion Funnel:")
        funnel = data.get('conversion_funnel', {})
        print(f"- Total Leads: {funnel.get('total_leads', 0)}")
        print(f"- Qualified Leads: {funnel.get('qualified_leads', 0)}")
        print(f"- Opportunities: {funnel.get('opportunities', 0)}")
        print(f"- Closed Deals: {funnel.get('closed_deals', 0)}")

    def _display_pipeline_report(self, data):
        print("\nStage Distribution:")
        for stage, count in data['stage_distribution'].items():
            print(f"- {stage}: {count}")
        print("\nValue by Stage:")
        for stage, value in data['value_by_stage'].items():
            print(f"- {stage}: R$ {value:.2f}")
        print(f"\nAverage Deal Size: R$ {data['average_deal_size']:.2f}")